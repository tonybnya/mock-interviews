import react from "/assets/react.svg";
import tailwind from "/assets/tailwind.svg";

const Navbar = () => {
  return (
    <nav className="flex flex-col gap-4 px-8 py-4 border-b-1 border-gray-900">
      <div className="flex gap-2">
        <a
          href="/"
          className="px-2 bg-white hover:bg-white/50 text-black flex items-center justify-center rounded-sm"
        >
          Home
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={react} className="logo react" alt="React logo" />
        </a>
        <a href="https://tailwindcss.com" target="_blank">
          <img src={tailwind} className="logo tailwind" alt="Tailwind logo" />
        </a>
      </div>
      <div>
        <h1 className="pb-0.5 font-bold">React + Tailwind Coding Interviews</h1>
      </div>
    </nav>
  );
};

export default Navbar;
