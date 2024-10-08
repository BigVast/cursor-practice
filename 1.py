<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>待办事项列表</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f7f7f7;
            color: #333;
        }
        .container {
            background-color: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }
        #task-form {
            display: flex;
            margin-bottom: 30px;
        }
        #task-input {
            flex-grow: 1;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 4px 0 0 4px;
            transition: border-color 0.3s;
        }
        #task-input:focus {
            outline: none;
            border-color: #3498db;
        }
        button {
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 0 4px 4px 0;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        #task-list {
            list-style-type: none;
            padding: 0;
        }
        .task-item {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            background-color: white;
            padding: 15px 15px 15px 10px;
            border-radius: 8px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .task-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 10px rgba(0,0,0,0.15);
        }
        .task-text {
            flex-grow: 1;
            margin-left: 15px;
            font-size: 18px;
        }
        .completed {
            text-decoration: line-through;
            color: #95a5a6;
        }
        .delete-btn {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .delete-btn:hover {
            background-color: #c0392b;
        }
        input[type="checkbox"] {
            width: 20px;
            height: 20px;
            margin-right: 10px;
        }
        .task-number {
            min-width: 24px;
            height: 24px;
            background-color: #3498db;
            color: white;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 14px;
            margin-right: 10px;
        }
        .task-content {
            display: flex;
            align-items: center;
            flex-grow: 1;
        }

        .timeline {
            display: flex;
            margin-top: 30px;
            background-color: #f9f9f9;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .timeline-day {
            flex: 1;
            padding: 15px;
            border-right: 1px solid #e0e0e0;
            transition: background-color 0.3s;
        }

        .timeline-day:last-child {
            border-right: none;
        }

        .timeline-day:hover {
            background-color: #f0f0f0;
        }

        .timeline-date {
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
            color: #3498db;
            font-size: 14px;
        }

        .timeline-tasks {
            list-style-type: none;
            padding: 0;
        }

        .timeline-task {
            background-color: #ffffff;
            border-radius: 6px;
            padding: 10px;
            margin-bottom: 10px;
            font-size: 14px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }

        .timeline-task:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .timeline-task.completed {
            text-decoration: line-through;
            color: #95a5a6;
            background-color: #f8f8f8;
        }

        .timeline-task-dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 8px;
            background-color: #3498db;
        }

        .timeline-task.completed .timeline-task-dot {
            background-color: #95a5a6;
        }

        .timeline-day.today {
            background-color: #e8f4fd;
        }

        .timeline-day.today .timeline-date {
            color: #2980b9;
        }

        .calendar {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .day {
            flex: 1;
            text-align: center;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .day:hover {
            background-color: #f0f0f0;
        }

        .day.selected {
            background-color: #3498db;
            color: white;
        }

        .day-name {
            font-weight: bold;
            margin-bottom: 5px;
        }

        .day-date {
            font-size: 12px;
        }

        #task-form {
            display: flex;
            flex-direction: column;
            margin-bottom: 30px;
        }

        #task-input {
            margin-bottom: 10px;
        }

        #add-task-btn {
            align-self: flex-end;
        }

        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            .container {
                padding: 15px;
            }
            h1 {
                font-size: 24px;
            }
            #task-form {
                flex-direction: column;
            }
            #task-input, #add-task-btn {
                width: 100%;
                margin-bottom: 10px;
                border-radius: 4px;
            }
            .task-item {
                flex-direction: column;
                align-items: flex-start;
            }
            .task-content {
                width: 100%;
                margin-bottom: 10px;
            }
            .delete-btn {
                align-self: flex-end;
            }
            .timeline {
                flex-direction: column;
            }
            .timeline-day {
                border-right: none;
                border-bottom: 1px solid #e0e0e0;
            }
            .timeline-day:last-child {
                border-bottom: none;
            }
            .calendar {
                flex-wrap: wrap;
            }
            .day {
                flex-basis: calc(33.33% - 10px);
                margin-bottom: 10px;
            }
        }

        @media (max-width: 480px) {
            .day {
                flex-basis: calc(50% - 10px);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>待办事项列表</h1>
        <div class="calendar" id="calendar"></div>
        <form id="task-form">
            <input type="text" id="task-input" placeholder="输入新任务" required>
            <button type="submit" id="add-task-btn">添加任务</button>
        </form>
        <ul id="task-list"></ul>
        <div class="timeline" id="timeline"></div>
    </div>

    <script>
        const taskForm = document.getElementById('task-form');
        const taskInput = document.getElementById('task-input');
        const taskList = document.getElementById('task-list');
        const calendar = document.getElementById('calendar');

        let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        let selectedDate = new Date();

        function renderCalendar() {
            calendar.innerHTML = '';
            const today = new Date();
            const weekStart = new Date(today);
            weekStart.setDate(today.getDate() - today.getDay());

            for (let i = 0; i < 7; i++) {
                const date = new Date(weekStart);
                date.setDate(weekStart.getDate() + i);
                const dayElement = document.createElement('div');
                dayElement.className = 'day';
                if (date.toDateString() === selectedDate.toDateString()) {
                    dayElement.classList.add('selected');
                }
                dayElement.innerHTML = `
                    <div class="day-name">${['日', '一', '二', '三', '四', '五', '六'][date.getDay()]}</div>
                    <div class="day-date">${date.getDate()}</div>
                `;
                dayElement.addEventListener('click', () => {
                    selectedDate = date;
                    renderCalendar();
                    renderTasks();
                });
                calendar.appendChild(dayElement);
            }
        }

        function renderTimeline() {
            const timeline = document.getElementById('timeline');
            timeline.innerHTML = '';

            const weekStart = new Date(selectedDate);
            weekStart.setDate(selectedDate.getDate() - selectedDate.getDay());

            for (let i = 0; i < 7; i++) {
                const date = new Date(weekStart);
                date.setDate(weekStart.getDate() + i);
                
                const dayElement = document.createElement('div');
                dayElement.className = 'timeline-day';
                if (date.toDateString() === new Date().toDateString()) {
                    dayElement.classList.add('today');
                }
                
                const dateElement = document.createElement('div');
                dateElement.className = 'timeline-date';
                dateElement.textContent = `${date.getMonth() + 1}月${date.getDate()}日 ${['周日', '周一', '周二', '周三', '周四', '周五', '周六'][date.getDay()]}`;
                dayElement.appendChild(dateElement);

                const taskList = document.createElement('ul');
                taskList.className = 'timeline-tasks';

                const dayTasks = tasks.filter(task => 
                    new Date(task.date).toDateString() === date.toDateString()
                );

                dayTasks.forEach(task => {
                    const taskElement = document.createElement('li');
                    taskElement.className = `timeline-task ${task.completed ? 'completed' : ''}`;
                    taskElement.innerHTML = `
                        <span class="timeline-task-dot"></span>
                        ${task.text}
                    `;
                    taskElement.addEventListener('click', () => toggleTask(task.id));
                    taskList.appendChild(taskElement);
                });

                dayElement.appendChild(taskList);
                timeline.appendChild(dayElement);
            }
        }

        function renderTasks() {
            taskList.innerHTML = '';
            const filteredTasks = tasks.filter(task => 
                new Date(task.date).toDateString() === selectedDate.toDateString()
            );
            filteredTasks.forEach((task, index) => {
                const li = document.createElement('li');
                li.className = 'task-item';
                li.innerHTML = `
                    <div class="task-content">
                        <span class="task-number">${index + 1}</span>
                        <input type="checkbox" ${task.completed ? 'checked' : ''}>
                        <span class="task-text ${task.completed ? 'completed' : ''}">${task.text}</span>
                    </div>
                    <button class="delete-btn">删除</button>
                `;
                
                const checkbox = li.querySelector('input[type="checkbox"]');
                checkbox.addEventListener('change', () => toggleTask(task.id));

                const deleteBtn = li.querySelector('.delete-btn');
                deleteBtn.addEventListener('click', () => deleteTask(task.id));

                taskList.appendChild(li);
            });
            renderTimeline();
        }

        function addTask(text) {
            const newTask = { 
                id: Date.now(), 
                text, 
                completed: false, 
                date: selectedDate.toISOString() 
            };
            tasks.push(newTask);
            saveTasks();
            renderTasks();
        }

        function toggleTask(id) {
            const task = tasks.find(t => t.id === id);
            if (task) {
                task.completed = !task.completed;
                saveTasks();
                renderTasks();
            }
        }

        function deleteTask(id) {
            tasks = tasks.filter(t => t.id !== id);
            saveTasks();
            renderTasks();
        }

        function saveTasks() {
            localStorage.setItem('tasks', JSON.stringify(tasks));
        }

        taskForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const text = taskInput.value.trim();
            if (text) {
                addTask(text);
                taskInput.value = '';
            }
        });

        renderCalendar();
        renderTasks();
    </script>
</body>
</html>








