document.addEventListener('DOMContentLoaded', function() {
    const taskList = document.getElementById('task-list');

    taskList.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const li = e.target.closest('li');
            const content = li.querySelector('.task-content').textContent;
            const newContent = prompt('Edit task', content);
            if (newContent) {
                editTask(li.dataset.id, newContent);
            }
        }
    });
});

function deleteTask(taskId) {
    fetch(`/delete/${taskId}`, {
        method: 'GET',
    }).then(response => {
        if (response.ok) {
            location.reload();
        }
    });
}

function editTask(taskId, newContent) {
    fetch(`/edit/${taskId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `content=${encodeURIComponent(newContent)}`,
    }).then(response => {
        if (response.ok) {
            location.reload();
        }
    });
}
