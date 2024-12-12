import { Form } from "@remix-run/react";
import { useState } from "react";

export default function Component() {
    const [formData, setFormData] = useState({
        temperature: '',
        humidity: '',
        windSpeed: '',
        precipitation: '',
        cloudCover: '',
        atmosphericPressure: '',
        uvIndex: '',
        season: '',
        visibility: '',
        location: ''
    });

    const [prediction, setPrediction] = useState<string | null>(null);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/predict/logistic_model', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ features: Object.values(formData).join(',') })
        });
        const result = await response.json();
        setPrediction(result["Predicted Class"]);
    };

    const getImageSrc = (weatherType: string) => {
        switch (weatherType) {
            case 'Rainy':
                return '/rainyModel.jpg';
            case 'Cloudy':
                return '/cloudyModel.jpeg';
            case 'Sunny':
                return '/sunnyModel.jpeg';
            case 'Snowy':
                return '/snowyModel.jpeg';
            default:
                return '';
        }
    }

    return (
        <div>
            <Form onSubmit={handleSubmit}>
                <div className="flex flex-row place-content-center pt-4">
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Temperature
                        </label>
                        <input type="text" name="temperature" value={formData.temperature} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Humidity
                        </label>
                        <input type="text" name="humidity" value={formData.humidity} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Wind Speed
                        </label>
                        <input type="text" name="windSpeed" value={formData.windSpeed} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Precipitation
                        </label>
                        <input type="text" name="precipitation" value={formData.precipitation} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Cloud Cover
                        </label>
                        <input type="text" name="cloudCover" value={formData.cloudCover} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                </div>
                <div className="flex flex-row place-content-center pt-4">
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Atmospheric Pressure
                        </label>
                        <input type="text" name="atmosphericPressure" value={formData.atmosphericPressure} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            UV Index
                        </label>
                        <input type="text" name="uvIndex" value={formData.uvIndex} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Season
                        </label>
                        <input type="text" name="season" value={formData.season} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Visibility
                        </label>
                        <input type="text" name="visibility" value={formData.visibility} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                    <div className="flex flex-col pt-4">
                        <label className="flex flex-row place-content-center text-lg font-bold">
                            Location
                        </label>
                        <input type="text" name="location" value={formData.location} onChange={handleChange} className="border-2 border-gray-300 rounded-lg p-2" />
                    </div>
                </div>
                <div className="flex flex-row place-content-center pt-4">
                    <button type="submit" className="bg-blue-500 text-white rounded-lg p-2">Submit</button>
                </div>
                <div className={prediction === null ? 'h-40' : 'hidden'}></div>
                <div className={prediction === null ? 'h-40' : 'hidden'}></div>
            </Form>
            {prediction && (
                <div>
                    <div className="flex flex-row place-content-center pt-4">
                        <h1 className="text-6xl font-bold">
                            The Weather is {prediction}
                        </h1>
                    </div>
                    <div className="flex flex-row place-content-center pt-4 pb-8">
                        <img src={getImageSrc(prediction)} alt={prediction} className="w-100 h-100" />
                    </div>
                </div>
            )}
        </div>
    );
}
