import pickle
class ML_Model_Loader:
    @staticmethod
    def save_model(model, filename):
        """Saves a model to a pickle file.

        Args:
            model: The model object to save.
            filename (str): The name of the file to save the model to.
        """
        with open(filename, 'wb') as file:
            pickle.dump(model, file)

    @staticmethod
    def load_model(filename):
        """Loads a model from a pickle file.

        Args:
            filename (str): The name of the file to load the model from.

        Returns:
            The loaded model.
        """
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        return model