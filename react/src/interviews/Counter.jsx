import { useState } from "react";

const Counter = () => {
  const [counter, setCounter] = useState(0);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <div className="flex justify-center items-center gap-8 pb-2">
        <button
          onClick={() => setCounter(counter - 1)}
          className="bg-yellow-500 px-2 py-0.5 min-w-[100px] text-4xl font-bold rounded-md cursor-pointer"
        >
          -
        </button>
        <span className="font-bold text-4xl">{counter}</span>
        <button
          onClick={() => setCounter(counter + 1)}
          className="bg-yellow-500 px-2 py-0.5 min-w-[100px] text-4xl font-bold rounded-md cursor-pointer"
        >
          +
        </button>
      </div>
      <button
        onClick={() => setCounter(0)}
        className="bg-red-500 px-2 py-2 min-w-[100px] text-xl font-bold rounded-md cursor-pointer"
      >
        Reset
      </button>
    </div>
  );
};

export default Counter;
