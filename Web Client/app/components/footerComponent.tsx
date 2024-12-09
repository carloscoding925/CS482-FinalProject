export default function FooterComponent() {
    return (
        <div>
            <footer className="h-[50px] flex flex-row justify-between">
                <div className="flex flex-row justify-left items-baseline space-x-10">
                    <h1 className="text-2xl">
                        Weather Classification
                    </h1>
                    <h1 className="text-xl">
                        © 2024 Weather Classification App
                    </h1>
                </div>
                <div className="flex flex-row justify-right">
                    <h1 className="text-2xl">
                        Made by Carlos Hernandez & Jonathan Nunez, CS 482
                    </h1>
                </div>
            </footer>
        </div>
    );
}