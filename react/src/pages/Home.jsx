import Task from "../components/Task";

const tasks = [
  {
    num: 1,
    title: "Counter",
    href: "counter",
    description:
      "Design and implement a React component that initializes a numerical counter at zero and provides a user interface with three distinct buttons: one to increment the current count by one each time it is clicked, another to decrement the count by one, and a third to reset the counter back to its original value of zero, ensuring the current count is always clearly displayed and updates responsively based on user interactions.",
  },
  {
    num: 2,
    title: "Random User API",
    href: "random-user-api",
    description:
      "Build a React component that fetches and displays random user data from the Random User API (https://randomuser.me/api). The component should make an API call when it mounts (using useEffect) and show key user information such as their full name, email, phone number, location (city, country), date of birth, and profile picture. Include a 'Get New User' button that triggers another API request to fetch and display a new random user. Ensure the UI is responsive and handles loading and error states gracefully.",
  },
];

const Home = () => {
  return (
    <div className="px-8 py-4 space-y-2">
      {tasks.map((task) => (
        <Task
          key={task.num}
          taskNumber={task.num}
          taskTitle={task.title}
          taskHref={task.href}
          taskDescription={task.description}
        />
      ))}
    </div>
  );
};

export default Home;
