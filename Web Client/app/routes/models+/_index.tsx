import { Link } from "@remix-run/react";

export default function Component() {
    return (
        <div>
            <div className="h-20">

            </div>
            <div className="flex flex-row place-content-center">
                <Link to="/models/logisticRegression">
                    <div className="bg-cover flex flex-col justify-end h-80 w-80" style={{ backgroundImage: `url('/logistic.jpeg')` }}>
                    
                    </div>
                    <h1 className="text-5xl font-bold hover:text-blue-600">
                        Logistic Regression
                    </h1>
                </Link>
                <Link to="/models/neuralNetwork">
                    <div className="bg-cover flex flex-col justify-end h-80 w-80 mr-40 ml-40" style={{ backgroundImage: `url('/neuralnetwork.jpeg')` }}>
                        
                    </div>
                    <h1 className="text-5xl font-bold mr-40 ml-40 hover:text-blue-600">
                        Neural Network
                    </h1>
                </Link>
                <Link to="/models/decisionTree">
                    <div className="bg-cover flex flex-col justify-end h-80 w-80" style={{ backgroundImage: `url('/tree.jpeg')` }}>
                        
                    </div>
                    <h1 className="text-5xl font-bold hover:text-blue-600">
                        Decision Tree
                    </h1>
                </Link>
            </div>
            <div className="h-40">

            </div>
        </div>
    );
}