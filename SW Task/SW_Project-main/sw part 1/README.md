# Data Processing Architecture

## Introduction
This project implements a data processing architecture consisting of three main modules: **Data Ingestor**, **Processing**, and **Output Producer**. Utilizing various design patterns, the architecture ensures flexibility, maintainability, and scalability, enabling efficient data handling from diverse sources to final output. Additionally, the code adheres to SOLID principles, promoting better software design practices.

## Design Patterns Overview

### Singleton Pattern
-The Singleton Pattern is utilized through a centralized `REGISTRY` dictionary for all data sources, ensuring a single instance accessible across the application. This promotes consistency and reduces memory usage.
-The Singleton Pattern is utilized through a centralized `REGISTRY` dictionary for all data sinks, ensuring a single instance accessible across the application. This promotes consistency and reduces memory usage.

### Factory Pattern
-Implemented in the `Data_Source_Factory` class, the Factory Pattern allows for the instantiation of various data source types without specifying the exact class, enhancing maintainability and scalability.
-Implemented in the `Data_Sink_Factory` class, the Factory Pattern allows for the instantiation of various data sink types without specifying the exact class, enhancing maintainability and scalability.

### Decorator Pattern
-The `__call__` method in the `MetaRegistry` class draws on principles of the Decorator Pattern by automatically adding registration behavior to classes as they are defined, extending functionality without altering core behavior.so once you create a new data source or new data sink , it will registor his self in auto way as once the class is created the call method is being called

### Metaclass Pattern
-The implementation of a Metaclass (MetaRegistry) showcases a powerful design pattern for customizing class creation. This allows for injecting additional behavior (registration) when a class is defined, serving as a factory for class creation.

### Abstract Factory Pattern (Implied)
-The overall structure of the data processing architecture aligns with the Abstract Factory Pattern. The `Data_Source` class serves as an abstract base, defining a family of data source products, while specific implementations (e.g., `TextDataSource`) act as concrete products created through the factory method.
-for  The `Data_Sink` class serves as an abstract base, defining a family of data sink products, while specific implementations (e.g., `MysqlDataSink`) act as concrete products created through the factory method.

### Chain of Responsibility Pattern
The flow from Data Ingestor to Processing and Output Producer illustrates this pattern, allowing each component to function independently while promoting a clear separation of responsibilities.

### Composite Pattern
The composition of the Data Ingestor, Processing, and Output Producer modules reflects the Composite Pattern. Each module can be developed and maintained separately while functioning cohesively within the system.

### Proxy Pattern
A Proxy Pattern is implemented in the Data Ingestor to enforce a delay, ensuring that data ingestion occurs every 5 seconds. This provides a surrogate to manage the timing of the data retrieval process.

### Extended Functionality with Decorator Pattern
The Decorator Pattern is employed in the parser to extend the functionality of expressions, allowing for greater flexibility in modifying how data is parsed without changing the original parser's implementation.

## SOLID Principles Adherence
- **Single Responsibility Principle**: Each class handles a distinct aspect of the workflow, such as data ingestion, processing, or output generation.
- **Open/Closed Principle**: Classes can be extended without modifying existing code.
- **Liskov Substitution Principle**: Subtypes can be substituted for their base types without altering program correctness.
- **Interface Segregation Principle**: Interfaces are minimal and specific, preventing classes from being forced to implement unnecessary methods.
- **Dependency Inversion Principle**: High-level modules depend on abstractions rather than concrete implementations.

## Database Setup
This project uses MySQL for data storage. To create the necessary database, execute the following commands in the MySQL command line:
```sql
mysql -u root -p
CREATE DATABASE assets_db;
USE assets_db;
```

### Configuration
In the `main.py` file, update the username and password to match your MySQL server credentials.

To view results in the database, use the following SQL command in the MySQL terminal:
```sql
SELECT * FROM assets_data;
```

### Skipping Database Setup
If you prefer to skip the database part and visualize the output, replace the `data_sink_args` in the `main.py` file from:
```python
data_sink_args=['Database']
```
to
```python
data_sink_args=['Raw']
```

## Adding New Operations
To add a new operation (e.g., a bitwise AND operation), follow these steps:

1. **Define Class**: Create a new class `And` in `tokens.py`.
   ```python
   class And(Token):
       token_type = 'AND'
       def __init__(self):
           super().__init__(self.token_type, '&')
   ```

2. **Define Operation**: Create `AndOp` in `my_operator.py`.
   ```python
   class AndOp(BinOp):
       def __init__(self, left, right):
           super().__init__(left, "&", right)
       def get_value(self):
           return self.left.get_value() & self.right.get_value()
       def __str__(self):
           return f"And({self.left}, {self.right})"
   ```

3. **Import Operation**: Import `AndOp` in `my_parser.py`.
   ```python
   from my_software.Software_Processing_Engine.my_operator import AndOp
   ```

4. **Define Factor**: Add `and_factor` method in `my_parser.py`.
   ```python
   def and_factor(self):
       self.eat("AND")
       return AndOp(left=self.factor(), right=None)
   ```

5. **Decorator Function**: Define and use a decorator to modify the `expr` method.
   ```python
   def add_and_operation(func):
       def wrapper(self, *args, **kwargs):
           node = func(self, *args, **kwargs)
           while self.current_token.token_type in ("PLUS", "MINUS", 'AND'):
               operation_name = self.current_token.token_type.capitalize() + 'Op'
               self.eat(self.current_token.token_type)
               operation_func = globals()[operation_name]
               node = operation_func(node, self.term())
           return node
       return wrapper

   @add_and_operation
   def expr(self):
   ```

**Note**: The software supports only integer operations. The result will be an integer unless the final operation is division, which may produce a float.

## Adding New Data Sources and New Sink Data Sources
To add a new data source:(example for that JsonDataSource)

1. **Create File**: Create a file named `SourcenameCreate.py`.
2. **Define Class**: Create a `SourcenameDataSource` class inheriting from `DataSource`.
3. **Update Factory**: Import the new class in the `Data_Source_Factory`.

For Data Sink: (example for this Raw_Data_Sink)
1. **Create File**: Create a file named `SinknameCreate.py`.
2. **Define Class**: Create a `SinknameDataSource` class inheriting from `DataSink`.
3. **Update Factory**: Import the new class in the `Data_Sink_Factory`.

## Video Example
To see the data processing architecture in action, watch the following video demonstration:
![Watch Video](example.mp4)

In this video,We will run the application, and visualize the output.
## Conclusion
This project leverages various design patterns to create a modular and extensible data processing architecture. By adhering to SOLID principles and providing clear guidelines for extending functionality, it supports efficient data handling and processing.
