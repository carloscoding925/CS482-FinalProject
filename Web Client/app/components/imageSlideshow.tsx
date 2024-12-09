import { useEffect, useState } from "react";

export default function ImageSlideshow() {
    const images = [
        'beach.jpeg',
        'snowy.jpeg',
        'rainycity.jpeg'
    ];
    const [currentIndex, setCurrentIndex] = useState<number>(0);

    useEffect(() => {
        const timeInterval = setInterval(() => {
            setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 3000);

        return () => clearInterval(timeInterval);
    }, []);

    return (
        <div>
            <div className="relative w-full h-screen overflow-hidden">
                {images.map((image, index) => (
                    <div 
                        key={index} 
                        className={`absolute inset-0 transition-opacity duration-1000 ${index === currentIndex ? 'opacity-100' : 'opacity-0'}`} 
                        style={{ backgroundImage: `url(${image})`, backgroundSize: 'cover', backgroundPosition: 'center' }}
                    >
                    </div>
                ))}
            </div>
        </div>
    );
}