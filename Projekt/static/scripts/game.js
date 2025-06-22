//VARIABLES
let turn = '';
let player = '';
let groupId = '';
let yourBoard;
let opponentBoard;
let isWinner = false;

const SHIPS_STATUSES = {
  FREE: 'FREE',
  OCCUPIED: 'OCCUPIED',
  HITTED: 'MISS_SHOT',
  SHIP_HITTED: 'SHIP_HIT',
  NOT_ALLOWED: 4,
};

btnStart.addEventListener('click', function () {
  let username = usernameInput.value;
  //player = username + ':' + connection.connectionId;
  player = username;
  startPage.classList.add('hidden');
  const d1 = prepareMatrixToSend();

  socket.emit('AddPlayer', { player: player, board: d1 });
});

socket.on('WaitingForPlayer', function () {
  pendingPage.classList.remove('hidden');
});

socket.on(
  'GameStarted',
  function (gameInfo ){
    console.log(gameInfo);

    pendingPage.classList.add('hidden');
    gamePage.classList.remove('hidden');
    groupId = gameInfo.groupName;

    firstPlayerName.innerHTML = gameInfo.firstPlayer;
    secondPlayerName.innerHTML = gameInfo.secondPlayer;
  }
);

socket.on('WinnerInfo', function (winner) {
  turnActive.innerHTML = 'Winner: ' + winner;
  isWinner = true;
});

socket.on('GameStatus', function (gameStatus) {
  console.log('GAME STATUS', gameStatus)
  turn = gameStatus.turn;

  yourBoard = JSON.parse(gameStatus.playerBoard);
  opponentBoard = JSON.parse(gameStatus.opponentBoard);

  genBoard(leftBoard, yourBoard);
  genBoard(rightBoard, opponentBoard);

  const msg = turn === player ? 'Your shot' : 'Opponent move';
  turnActive.innerHTML = msg;

  const oppTest = rightBoard.childNodes;

  if (turn === player && !isWinner) {
    oppTest.forEach((el) => {
      if (!el.classList.contains('pppp') && !el.classList.contains('shoted')) {
        el.addEventListener('click', function () {
          socket.emit('Shot', {
            groupName: groupId,
            player: player,
            y: this.dataset.y,
            x: this.dataset.x,
          });
        });
      }
    });
  }
});

function genBoard(domElement, arr) {
  domElement.innerHTML = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      const field = document.createElement('div');
      field.classList.add('field');
      field.dataset.x = j;
      field.dataset.y = i;

      const div = document.createElement('div');

      if (arr[i][j] === SHIPS_STATUSES.OCCUPIED) {
        field.classList.add('taken');
      } else if (arr[i][j] === SHIPS_STATUSES.HITTED) {
        div.classList.add('shooted_div');
        field.classList.add('shoted');
        field.appendChild(div);
      } else if (arr[i][j] === SHIPS_STATUSES.SHIP_HITTED) {
        div.classList.add('shooted_hited');
        field.classList.add('pppp');
        field.classList.add('taken');
        div.textContent = 'X';
        field.appendChild(div);
      } else if (arr[i][j] === SHIPS_STATUSES.NOT_ALLOWED) {
        div.classList.add('tkn');
        field.classList.add('pppp');
        field.classList.add('taken');
        div.textContent = '--';
        field.appendChild(div);
      }

      domElement.appendChild(field);
    }
  }
}

socket.on('InfoAboutOpponentLeave', function (msg) {
  console.log(msg);
  isWinner = true;
});

msgForm.addEventListener('submit', function (e) {
  e.preventDefault();
  const x = msgValue.value;

  socket.emit('SendMessageToGroupChat', { groupName: groupId, player: player, message: x });

  msgValue.value = '';
});

socket.on('Message', function (message) {
  const div = document.createElement('div');

  const userInfoDiv = document.createElement('div');
  const msgTxt = document.createElement('div');

  userInfoDiv.textContent = `${new Date().getHours()}:${new Date().getMinutes()} ${
    message.player
  }: `;
  msgTxt.textContent = `${message.message}`;

  div.classList.add('chatMsg');
  div.appendChild(userInfoDiv);
  div.appendChild(msgTxt);

  chat.appendChild(div);
  chat.scrollBy(0, 100);
});

// window.addEventListener('beforeunload', function (event) {
//   if (player) {
//     event.preventDefault();
//     socket.emit('disconnect_from_group', { groupId, player });
//   }
// });
