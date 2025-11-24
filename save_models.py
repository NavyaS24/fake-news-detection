"""
Helper script to save your trained models and vectorizer.
Run this after training your models to save them for the Gradio app.
"""
import pickle

# After training your vectorizer (from your training code):
# vectorization = TfidfVectorizer()
# xv_train = vectorization.fit_transform(x_train)

# Save the vectorizer
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorization, f)
print("Vectorizer saved as vectorizer.pkl")

# After training any of your models, save it as model.pkl
# Choose ONE of the following based on which model performed best:

# Option 1: Save Logistic Regression
# with open('model.pkl', 'wb') as f:
#     pickle.dump(LR, f)

# Option 2: Save Decision Tree
# with open('model.pkl', 'wb') as f:
#     pickle.dump(DT, f)

# Option 3: Save Gradient Boosting
# with open('model.pkl', 'wb') as f:
#     pickle.dump(GB, f)

# Option 4: Save Random Forest (recommended)
with open('model.pkl', 'wb') as f:
    pickle.dump(RF, f)
print("Model saved as model.pkl")

print("\nBoth files saved! You can now run the Gradio app with:")
print("python gradio_app.py")
