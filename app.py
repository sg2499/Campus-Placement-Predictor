from flask import Flask, request, render_template
import pickle

# 📦 Load the trained Random Forest model from disk
file = open('CPP.pkl', 'rb')
rf = pickle.load(file)
file.close()

# 🌐 Initialize the Flask application
app = Flask(__name__)

# 📍 Define the route for the home page (handles both GET and POST requests)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    # Handle form submission
    if request.method == 'POST':
        # Step 1: Retrieve form data submitted by the user
        mydict = request.form

        # Step 2: Convert form inputs into the appropriate types
        gender = int(mydict['gender'])
        spec = int(mydict['spec'])
        tech = int(mydict['tech'])
        work = int(mydict['work'])
        ssc = float(mydict['ssc'])
        hsc = float(mydict['hsc'])
        dsc = float(mydict['dsc'])
        mba = float(mydict['mba'])

        # Step 3: Format input features as a list of lists for model prediction
        inputfeatures = [[gender, spec, tech, work, ssc, hsc, dsc, mba]]

        # Step 4: Make the prediction (0 or 1)
        predictedclass = rf.predict(inputfeatures)

        # Step 5: Predict the probability of placement
        predictedprob = rf.predict_proba(inputfeatures)

        # Step 6: Extract the relevant class probability
        if predictedclass[0] == 1:
            proba = predictedprob[0][1]  # Probability of 'Placed'
        else:
            proba = predictedprob[0][0]  # Probability of 'Not Placed'

        # Step 7: Map class prediction to human-readable message
        placemap = {1: 'Will be Placed', 0: 'Better Luck Next Time :('}
        predictedclasssend = placemap[predictedclass[0]]

        # Step 8: Render results on 'show.html' template with placement probability
        if predictedclass[0] == 1:
            return render_template(
                'show.html',
                predictedclasssend=predictedclasssend,
                predictedprob=round(proba * 100, 2),
                placed=True
            )
        else:
            return render_template(
                'show.html',
                predictedclasssend=predictedclasssend
            )

    # Render the input form on initial GET request
    return render_template('index.html')

# ▶️ Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)