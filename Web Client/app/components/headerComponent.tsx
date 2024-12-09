import { Link } from "@remix-run/react";

export default function HeaderComponent() {
    return (
        <div>
            <header className="bg-cover bg-center h-48 text-white flex flex-row" style={{ backgroundImage: `url('/banner.jpeg')` }}>
                <div className="w-full flex flex-row justify-start">
                    <div className="flex flex-col justify-end h-full">
                        <h1 className="font-serif text-6xl">
                            Weather Classification
                        </h1>
                    </div>
                </div>
                <div className="w-full flex flex-row justify-end">
                    <div className="flex flex-row space-x-10">
                        <h1 className="text-2xl flex flex-col justify-end">
                            <Link to={`/`}>
                                Home
                            </Link>
                        </h1>
                        <h1 className="text-2xl flex flex-col justify-end">
                            <Link to={`../models/`}>
                                Models
                            </Link>
                        </h1>
                        <h1 className="text-2xl flex flex-col justify-end pr-6">
                            <Link to={`/about`}>
                                About
                            </Link>
                        </h1>
                    </div>
                </div>
            </header>
        </div>
    );
}