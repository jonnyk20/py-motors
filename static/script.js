const motors = document.querySelectorAll('.motor');
const formatCommand = id => {
  console.log(id);
  const [motorId, command] = id.split('-');
  return {
    motorId,
    command
  };
};

const toggleMotor = ({ target: { id } }) =>
  fetch('/toggle', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify(formatCommand(id))
  });

motors.forEach(button => {
  button.addEventListener('click', toggleMotor);
});

const move = ({ target: { id } }) =>
  fetch('/move', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify({ direction: id })
  });

const directions = document.querySelectorAll('.direction');

directions.forEach(button => {
  button.addEventListener('click', move);
});
