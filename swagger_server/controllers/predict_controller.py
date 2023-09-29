import connexion
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util

from swagger_server.libs.data_preparation import generate_regression_data
from swagger_server.libs.model import create_regression_model
from swagger_server.libs.train import train_regression_model
from swagger_server.libs.predict import predict_regression

def get_predict_result(test_data):  # noqa: E501
    """Get prediction result

    Returns a single result 
    """
    # Generate synthetic regression data
    X_train, y_train = generate_regression_data()

    # Create and train the regression model
    regression_model = create_regression_model(X_train.shape[1:])
    train_regression_model(regression_model, X_train, y_train, epochs=100, batch_size=32)

    # Perform regression prediction
    sample_input = [[float(test_data)]]  # Example input for prediction
    predicted_value = predict_regression(regression_model, sample_input)

    return str(predicted_value)
