function addStaff(proj_id, csrf_token){
    const emp = document.getElementById('input-add-staff');
    const data = {
        projec : proj_id,
    };
    
    // กำหนด path ให้ถูกต้อง
    fetch(`/staff/proj/${proj_id}/emp/${emp.value}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message)
        }
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}

async function removeStaff(emp_Id, proj_id, csrf_token){

    // กำหนด path ให้ถูกต้อง
    fetch(`/staff/proj/${proj_id}/emp/${emp_Id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message)
        }
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}
