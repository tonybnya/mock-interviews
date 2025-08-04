const Task = ({ taskNumber, taskTitle, taskHref, taskDescription }) => {
  return (
    <a
      href={taskHref}
      className="block border border-gray-800 rounded-md p-4 hover:bg-gray-900 transition duration-200"
    >
      <div className="flex flex-col sm:flex-row sm:items-stretch gap-3">
        <span className="flex items-center justify-center w-12 h-10 bg-gray-950 text-white text-sm font-bold rounded-sm text-center">
          {taskNumber}
        </span>
        <h2 className="flex items-center px-3 bg-gray-950 h-10 text-white font-semibold rounded-sm text-lg sm:text-xl w-full">
          {taskTitle}
        </h2>
      </div>
      <p className="mt-3 text-sm text-gray-400 px-3 py-2 bg-gray-950 rounded-sm leading-relaxed">
        {taskDescription}
      </p>
    </a>
  );
};

export default Task;
