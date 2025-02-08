
function getNow() {
  const date = new Date();
  return {
    h: date.getHours().toString().padStart(2, 0),
    m: date.getMinutes().toString().padStart(2, 0),
    s: date.getSeconds().toString().padStart(2, 0),
  }
}

timeEl = document.getElementById('time');
const {h, m, s} = getNow();
timeEl.innerHTML = `${h}:${m}:${s}`

setInterval(() => {
  const {h, m, s} = getNow();
  timeEl.innerHTML = `${h}:${m}:${s}`
}, 1000)