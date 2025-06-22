const socket = io();

const SHIPS_DIRECTION = {
  vertical: 'vertical',
  horizontal: 'horizontal',
};

let draggedShip;
let shipsDriection = SHIPS_DIRECTION.vertical;
const size = 10;
const board = [];
let shipNameWithPicedPart = {};

const shipsOnBoard = [];

socket.on('connect', () => {});

socket.on('Ships', function (ships1) {
  ships1.forEach((ship) => {
    const div = document.createElement('div');
    div.classList.add('ship');
    div.setAttribute('id', ship.id);
    div.setAttribute('draggable', true);
    for (let i = 0; i < ship.length; i++) {
      const div1 = document.createElement('div');
      div1.classList.add('two');
      div1.setAttribute('data-id', i);
      div.appendChild(div1);
    }

    div.addEventListener('dragstart', dragStart);

    div.addEventListener('mousedown', (e) => {
      shipNameWithPicedPart.name = e.target.dataset.name;
      shipNameWithPicedPart.id = e.target.dataset.id;
    });

    ships.appendChild(div);
  });
});

//FUNCTIONS AND LOGIC
[...availableShips].forEach((ship) => {
  ship.addEventListener('dragstart', dragStart);
  ship.addEventListener('mousedown', (e) => {
    shipNameWithPicedPart.name = e.target.dataset.name;
    shipNameWithPicedPart.id = e.target.dataset.id;
  });
});

btnRotate.addEventListener('click', function () {
  [...availableShips].forEach((ship) => {
    ship.classList.toggle('shipHorizontal');
  });
  availableShips[0]?.classList.contains('shipHorizontal')
    ? (shipsDriection = SHIPS_DIRECTION.horizontal)
    : (shipsDriection = SHIPS_DIRECTION.vertical);
});

function dragStart(e) {
  draggedShip = e.target;
}

function dragOver(e) {
  e.preventDefault();
}

function dragEnter(e) {
  e.preventDefault();
}

function dragDrop(e) {
  e.preventDefault();
  let shipsInfo = [];

  const lengthOfDraggedShip = draggedShip.children.length;

  const startX = this.dataset.x - shipNameWithPicedPart.id;
  const startY = this.dataset.y - shipNameWithPicedPart.id;

  const endX = startX + lengthOfDraggedShip;
  const endY = startY + lengthOfDraggedShip;

  if (shipsDriection === SHIPS_DIRECTION.vertical) {
    if (
      validateShip(
        SHIPS_DIRECTION.vertical,
        startX,
        startY,
        endX,
        endY,
        this.dataset
      )
    ) {
      for (let i = 0; i < lengthOfDraggedShip; i++) {
        board[this.dataset.y][startX + i].classList.add('taken');
        shipsInfo.push({
          x: Number(this.dataset.y),
          y: Number(startX + i),
        });
      }
      const ship = new Ship(lengthOfDraggedShip, shipsInfo, draggedShip.id);
      shipsOnBoard.push(ship);

      shipsInfo = [];
      draggedShip.setAttribute('draggable', false);
      draggedShip.classList.add('hidden1');
      printByShipObject();
    }
  } else {
    if (
      validateShip(
        SHIPS_DIRECTION.horizontal,
        startX,
        startY,
        endX,
        endY,
        this.dataset
      )
    ) {
      for (let i = 0; i < lengthOfDraggedShip; i++) {
        board[startY + i][this.dataset.x].classList.add('taken');
        shipsInfo.push({
          x: Number(startY + i),
          y: Number(this.dataset.x),
        });
      }
      const ship = new Ship(lengthOfDraggedShip, shipsInfo, draggedShip.id);
      shipsOnBoard.push(ship);

      shipsInfo = [];
      draggedShip.setAttribute('draggable', false);
      draggedShip.classList.add('hidden1');
      printByShipObject();
    }
  }
}

function dragEnd(e) {
  e.preventDefault();
}

function markNotAllowedFields() {
  const x = [];
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (board[i][j].classList.contains('notallowed')) {
        board[i][j].classList.remove('notallowed');
        board[i][j].innerHTML = '';
      }

      if (board[i][j].classList.contains('taken')) {
        if (i + 1 < size) {
          board[i + 1][j] ? x.push(board[i + 1][j]) : null;
          board[i + 1][j + 1] ? x.push(board[i + 1][j + 1]) : null;
          board[i + 1][j - 1] ? x.push(board[i + 1][j - 1]) : null;
        }
        if (i !== 0) {
          board[i - 1][j] ? x.push(board[i - 1][j]) : null;
          board[i - 1][j + 1] ? x.push(board[i - 1][j + 1]) : null;
          board[i - 1][j - 1] ? x.push(board[i - 1][j - 1]) : null;
        }

        board[i][j - 1] ? x.push(board[i][j - 1]) : null;
        board[i][j + 1] ? x.push(board[i][j + 1]) : null;
      }
    }
  }

  x.forEach((el) => {
    const dd = document.createElement('div');
    // dd.textContent = 'X';
    if (!el.children.length) el.appendChild(dd);
    el.classList.add('notallowed');
  });
}

function printByShipObject() {
  markNotAllowedFields();
  shipsOnBoard.forEach((ship) => {
    ship.positions.forEach((position) => {
      if (board[position.x][position.y].classList.contains('taken')) {
        if (board[position.x][position.y].classList.contains('notallowed')) {
          board[position.x][position.y].classList.remove('notallowed');
          board[position.x][position.y].innerHTML = '';
        }
      }
      board[position.x][position.y].addEventListener('click', () => {
        returnShip(ship);
      });
      board[position.x][position.y].classList.add('taken');
    });
  });
}

function returnShip(ship) {
  const d = shipsOnBoard.indexOf(ship);
  if (d >= 0) {
    availableShips[ship.id].classList.remove('hidden1');
    availableShips[ship.id].setAttribute('draggable', true);

    shipsOnBoard[d].positions.forEach((position) => {
      board[position.x][position.y].classList.remove('taken');
    });
    shipsOnBoard.splice(d, 1);
    printByShipObject();
  }
}

function generateBoard() {
  for (let i = 0; i < size; i++) {
    board[i] = [];
    for (let j = 0; j < size; j++) {
      const field = document.createElement('div');
      field.classList.add('field');
      field.dataset.x = j;
      field.dataset.y = i;
      board[i][j] = field;

      field.addEventListener('dragover', dragOver);
      field.addEventListener('dragenter', dragEnter);
      field.addEventListener('drop', dragDrop);
      field.addEventListener('dragend', dragEnd);
      boardTemplate.appendChild(field);
    }
  }
}

function prepareMatrixToSend() {
  const exportBoard = [];
  for (let i = 0; i < size; i++) {
    exportBoard[i] = [];
    for (let j = 0; j < size; j++) {
      if (board[i][j].classList.contains('taken')) {
        exportBoard[i][j] = 1;
      } else {
        exportBoard[i][j] = 0;
      }
    }
  }
  return exportBoard;
}

function validateShip(direction, startX, startY, endX, endY, dataset) {
  switch (direction) {
    case SHIPS_DIRECTION.vertical:
      if (
        startX >= 0 &&
        endX <= size &&
        !board[dataset.y][startX].children.length &&
        !board[dataset.y][startX].classList.contains('taken') &&
        !board[dataset.y][endX - 1].children.length &&
        !board[dataset.y][endX - 1].classList.contains('taken')
      )
        return true;
      return false;
    case SHIPS_DIRECTION.horizontal:
      if (
        startY >= 0 &&
        endY <= size &&
        !board[endY - 1][dataset.x].children.length &&
        !board[endY - 1][dataset.x].classList.contains('taken') &&
        !board[startY][dataset.x].classList.contains('taken') &&
        !board[startY][dataset.x].children.length
      )
        return true;
      return false;
  }
}

window.addEventListener('DOMContentLoaded', generateBoard());
