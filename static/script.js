const onButton = document.getElementById('on-button');
const offButton = document.getElementById('off-button');
const onClick = async () => {
  const res = await fetch('/test', {
    method: 'POST',
    body: JSON.stringify({ msg: 'Hello again from client' }),
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
      // "Content-Type": "application/x-www-form-urlencoded",
    }
  });
  console.log('res', res);
  const text = await res.text();
  console.log('text:', text);
};

const turnOn = async () => {
  const res = await fetch('/on');
  const text = await res.text();
  console.log(text);
};

const turnOff = async () => {
  const res = await fetch('/off');
  const text = await res.text();
  console.log(text);
};

onButton.addEventListener('click', turnOn);
offButton.addEventListener('click', turnOff);
