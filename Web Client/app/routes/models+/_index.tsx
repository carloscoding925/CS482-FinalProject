import { Link } from "@remix-run/react";

export default function Component() {
    return (
        <div>
            <div className="flex flex-row place-content-center">
                <div className="flex flex-col h-80 w-80" style={{ backgroundImage: `url('/logistic.jpeg')` }}>
                    
                </div>
                <div className="flex flex-col h-80 w-80 mr-40 ml-40" style={{ backgroundImage: `url('/neuralnetwork.jpeg')` }}>

                </div>
                <div className="flex flex-col h-80 w-80" style={{ backgroundImage: `url('/tree.jpeg')` }}>

                </div>
            </div>
        </div>
    );
}