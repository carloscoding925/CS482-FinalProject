# Welcome to our CS 482 Final Project

- Carlos Hernandez & Jonathan Nunez

# For the teaching team

- Our code for the AI models is under the following folder <br/>
- `API -> models` Which has our Decision_Tree, Logistic_Regression, and Neural_Network files

- app.py is the only other file in the `API` folder which is built by us, the rest of the files are system generated

- For the `Web-Client` folder, all the files in the `components` and `routes` folders are built by us along with <br/>
- `root.tsx` in the `app` folder. The rest of the files are system generated. 

# How to run Web Client

- In terminal, navigate to `Web Client` folder and run the following
- `npm install`
- `npm run dev`

# How to run API

- The virtual environment is NOT included in the github repo

- In terminal, navigate to `API` folder and run the following

- If you havent added a virtual environment yet, do this first

- `python3 -m venv virtual-env`

- Now you can do the following

- `source virtual-env/bin/activate`
- `pip install fastapi`
- Go ahead and do pip install for `numpy`, `pandas`, `scikit-learn`, `matplotlib`, and `torch`

- Now you can do these commands
- `source virtual-env/bin/activate` If you havent already
- `fastapi dev app.py`

- Once finished, you can do ctrl + c to stop both servers (do it in each terminal, API and Web Client)
- Run `deactivate` in the API terminal to stop the virtual env.
