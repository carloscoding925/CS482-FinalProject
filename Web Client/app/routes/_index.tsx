import { Link } from "@remix-run/react";
import ImageSlideshow from "~/components/imageSlideshow";

export default function Component() {
  return (
    <div>
      <div className="flex flex-row place-content-center">
        <div className="flex flex-col">
          <h1 className="text-4xl flex place-content-center">
            Welcome!
          </h1>
          <h1 className="text-4xl">
            Determine the weather outside using machine learning.
          </h1>
          <h1 className="text-4xl flex place-content-center">
            To get started
          </h1>
          <h1 className="text-4xl flex place-content-center hover:text-blue-400 transition-colors duration-300">
            <Link to="/models">
              Click Here
            </Link>
          </h1>
        </div>
      </div>
      <ImageSlideshow />
    </div>
  )
}