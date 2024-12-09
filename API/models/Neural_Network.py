# -*- coding: utf-8 -*-
"""model_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iRJFrs9lfO4959h--PrtY6BS7cukf8cn
"""

# Import dependencies
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt

# Load and preprocess data
def preprocess_data(path):
    path = "/content/drive/My Drive/Cs482/Assignments/Final/model_01/weather_classification_data.csv"
    data = pd.read_csv(path)
    X = data.drop('Weather Type', axis=1)
    y = data['Weather Type']
    X = pd.get_dummies(X, columns=['Cloud Cover', 'Season', 'Location'], drop_first=True)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = torch.tensor(X_scaled, dtype=torch.float32)
    y_encoded = torch.tensor(y_encoded, dtype=torch.long)
    return X_scaled, y_encoded, label_encoder

# Define the neural network
class MultiLayerNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(MultiLayerNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        out = torch.relu(self.fc1(x))
        out = torch.relu(self.fc2(out))
        out = self.fc3(out)
        return out

# Training function
def train_network(model, optimizer, criterion, X_train, y_train, X_val, y_val, num_epochs):
    train_losses = torch.zeros(num_epochs)
    val_losses = torch.zeros(num_epochs)
    train_accuracies = torch.zeros(num_epochs)
    val_accuracies = torch.zeros(num_epochs)

    for epoch in range(num_epochs):
        # Training phase
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

        # Store training loss
        train_losses[epoch] = loss.item()

        # Training accuracy
        _, predicted = torch.max(outputs, 1)
        correct = (predicted == y_train).sum().item()
        train_accuracies[epoch] = correct / len(y_train)

        # Validation phase
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_val)
            val_loss = criterion(val_outputs, y_val)
            val_losses[epoch] = val_loss.item()

            # Validation accuracy
            _, val_predicted = torch.max(val_outputs, 1)
            val_correct = (val_predicted == y_val).sum().item()
            val_accuracies[epoch] = val_correct / len(y_val)

        # Print epoch information
        if epoch % 5 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Training Loss: {train_losses[epoch]:.4f}, "
                  f"Validation Loss: {val_losses[epoch]:.4f}, "
                  f"Training Accuracy: {train_accuracies[epoch]:.4f}, "
                  f"Validation Accuracy: {val_accuracies[epoch]:.4f}")

    return train_losses, val_losses, train_accuracies, val_accuracies

# Evaluation function
def evaluate_model(model, X, y, label_encoder):
    model.eval()
    with torch.no_grad():
        outputs = model(X)
        _, predicted = torch.max(outputs, 1)
        accuracy = accuracy_score(y, predicted)
        precision = precision_score(y, predicted, average='weighted')
        recall = recall_score(y, predicted, average='weighted')
        f1 = f1_score(y, predicted, average='weighted')
    return accuracy, precision, recall, f1

# Plotting function
def plot_metrics(train_losses, val_losses, train_accuracies, val_accuracies, num_epochs):
    # Plotting loss
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_epochs), train_losses, label='Training Loss', color='gold', marker='o')
    plt.plot(range(num_epochs), val_losses, label='Validation Loss', color='darkorange', marker= 's')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Train and Validation Loss over Epochs')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plotting accuracy
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_epochs), train_accuracies, label='Training Accuracy',  color='gold', marker='o')
    plt.plot(range(num_epochs), val_accuracies, label='Validation Accuracy', color='darkorange', marker= 's')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Train and Validation Accuracy over Epochs')
    plt.legend()
    plt.grid(True)
    plt.show()

def evaluate_model(model, X, y, label_encoder):
    model.eval()
    with torch.no_grad():
        predictions = model(X)
        predicted_labels = torch.argmax(predictions, dim=1).numpy()
        true_labels = y.numpy()

    # Calculate metrics
    accuracy = accuracy_score(true_labels, predicted_labels)
    precision = precision_score(true_labels, predicted_labels, average="weighted", zero_division=0)
    recall = recall_score(true_labels, predicted_labels, average="weighted", zero_division=0)
    f1 = f1_score(true_labels, predicted_labels, average="weighted", zero_division=0)

    # Display the classification report for detailed metrics
    print("\nClassification Report:\n")
    print(classification_report(true_labels, predicted_labels, target_names=label_encoder.classes_))

    # Return metrics as a dictionary
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }



# Main execution
if __name__ == "__main__":
    # Data preprocessing
    path = "/content/drive/My Drive/Cs482/Assignments/Final/model_01/weather_classification_data.csv"
    X_scaled, y_encoded, label_encoder = preprocess_data(path)

    # Train-test split
    X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Model setup and training
    model_mln = MultiLayerNet(input_dim=X_train.shape[1], output_dim=len(label_encoder.classes_))
    optimizer = optim.Adam(model_mln.parameters(), lr=0.03)
    loss_fn = nn.CrossEntropyLoss()
    num_epochs = 35

    # Train the network and get metrics
    train_losses, val_losses, train_accuracies, val_accuracies = train_network(
        model_mln, optimizer, loss_fn, X_train, y_train, X_val, y_val, num_epochs)

    # Evaluate model
    # Evaluate the trained model on the test set
    evaluation_results = evaluate_model(model_mln, X_test, y_test, label_encoder)

    # Print evaluation results
    print("\nEvaluation Metrics:")
    for metric, value in evaluation_results.items():
        print(f"{metric.capitalize()}: {value:.4f}")

    plot_metrics(train_losses, val_losses, train_accuracies, val_accuracies, num_epochs)
    '''torch.save({
            'epoch': num_epochs,
            'model_state_dict': model_mln.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': train_losses[-1],
            }, '/content/drive/My Drive/Cs482/Assignments/Final/mln.pt')'''

torch.save({
            'epoch': num_epochs,
            'model_state_dict': model_mln.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': train_losses[-1],
            }, '/content/drive/My Drive/Cs482/Assignments/Final/mln.pth')