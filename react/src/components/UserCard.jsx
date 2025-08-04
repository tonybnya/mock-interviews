const UserCard = ({
  firstName,
  lastName,
  email,
  phone,
  city,
  state,
  country,
  dob,
  age,
  profile,
}) => {
  return (
    <div className="flex flex-col items-center gap-4 bg-gray-950 p-6 rounded-md shadow-md max-w-md mx-auto">
      <img
        className="w-32 h-32 rounded-full object-cover"
        src={profile}
        alt="Profile"
      />
      <div className="text-left w-full space-y-1">
        <div className="flex items-center gap-2">
          <span>👤</span>
          <h3 className="font-bold text-lg">
            {firstName} {lastName}
          </h3>
        </div>
        <div className="flex items-center gap-2">
          <span>✉️</span>
          <p>{email}</p>
        </div>
        <div className="flex items-center gap-2">
          <span>📞</span>
          <p>{phone}</p>
        </div>
        <div className="flex items-center gap-2">
          <span>🗺️</span>
          <p>
            {city}, {state}, {country}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span>🎂</span>
          <p>
            {dob} (Age: {age})
          </p>
        </div>
      </div>
    </div>
  );
};

export default UserCard;
