from sklearn.metrics import classification_report, accuracy_score,f1_score,confusion_matrix

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nconfusion matrix:\n", confusion_matrix(y_test, y_pred))
    print("\ f1 score:\n", f1_score(y_test, y_pred))
