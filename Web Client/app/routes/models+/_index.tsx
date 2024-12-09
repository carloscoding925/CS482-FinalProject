import { Link } from "@remix-run/react";

export default function Component() {
    return (
        <div>
            <Link to={`../models/modelOne`}>
                Link
            </Link>
        </div>
    );
}