const input = document.getElementById("inputTask");
const btn = document.getElementById("btn");
const taskList = document.getElementById("taskList");


const displayTasks = () =>{
    const tasks = JSON.parse(localStorage.getItem("tasks"));
    taskList.innerHTML = "";
    for (const task of tasks){
        const taskElement = document.createElement("div")
        const taskName = document.createElement("span")
        const taskStatus = document.createElement("span")
        const taskRemove = document.createElement("button")
        const taskMark = document.createElement("button");


        taskName.textContent = task.taskName;
        taskStatus.textContent = `Done: ${task.done}`
        taskRemove.textContent = "X";
        taskMark.textContent = "Change status";

        taskRemove.addEventListener("click",()=>removeTask(task?.taskId))
        taskMark.addEventListener("click",()=>changeStatus(task?.taskId));


        taskElement.appendChild(taskName);
        taskElement.appendChild(taskStatus);
        taskElement.appendChild(taskMark)
        taskElement.appendChild(taskRemove);
        taskElement.classList.add("task")
        taskList.appendChild(taskElement)
    }
}

(()=>{
    const tasks = JSON.parse(localStorage.getItem("tasks"));
    if(!tasks){
        localStorage.setItem("tasks",JSON.stringify([]));
    }
    else {
        displayTasks();
    }
})()


function removeTask (taskId){
    const tasks = JSON.parse(localStorage.getItem("tasks"));
    const updated =  tasks.filter(task => task.taskId!==taskId);
    localStorage.setItem("tasks",JSON.stringify(updated))
    displayTasks();
}

function changeStatus(taskId){
    const tasks = JSON.parse(localStorage.getItem("tasks"));
    const toUpdate = tasks.find(task => task.taskId === taskId);
    toUpdate.done = !toUpdate.done;
    localStorage.setItem("tasks",JSON.stringify(tasks))
    displayTasks();
}

btn.addEventListener("click",(e)=>{
    e.preventDefault()
    if(input.value){
        const tasks = JSON.parse(localStorage.getItem("tasks"));
        const task = {
            taskId: crypto.randomUUID(),
            taskName: input.value,
            done: false
        }
        tasks.push(task);
        localStorage.setItem("tasks",JSON.stringify(tasks))
        input.value = "";
        displayTasks()
    }
})


