export default function TextBox() {
    return (
        <div>
            <div className="flex flex-col items-center justify-center min-h-screen">
                <div className="w-[1000px] h-[600px] border border-gray-300 flex items-start justify-center">
                    <div className="text-center">
                        <h1 className="text-4xl pt-6">
                            About
                        </h1>
                        <p className="pt-6 pl-6 pr-6">
                            Welcome to the Weather Classification Website! This project was created by Carlos Hernandez and Jonathan Nunez as the final project
                            for CS 482 - Introduction to AI at the University of Nevada, Reno. The goal of this project is to recieve metrics about the current weather
                            or to have a user enter metrics for weather and return a classification of the weather type. This project consists of two parts: the web client
                            and the API service. The Web Client is built using React and the Remix framework and the API is built using Python and the Python FastAPI Library.
                            We hope you enjoy using our website and find it useful!
                        </p>
                        <div className="pt-4 flex flex-row place-content-center">
                            <div className="flex flex-row h-[300px] w-[300px] bg-cover bg-center" style={{ backgroundImage: `url('/favicon.ico')` }}>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}