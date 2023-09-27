document.getElementById('id_date').placeholder = '{{ form.instance.date}}';
document.getElementById('id_time').placeholder = '{{ form.instance.get_time_display}}';
document.getElementById('id_num_guests').placeholder = '{{ form.instance.num_guests}}';
document.getElementById('id_table').placeholder = '{{ form.instance.table}}';
document.getElementById('id_notes').placeholder = '{{ form.instance.notes}}';

 // JavaScript to prevent selecting a past date
 const dateInput = document.getElementById("{{ form.date.auto_id }}");
 dateInput.addEventListener('change', function() {
     const today = new Date().toISOString().split('T')[0];
     if (dateInput.value < today) {
         dateInput.value = today;
     }
 });

 // JavaScript to prevent selecting a past time
 const timeInput = document.getElementById("{{ form.time.auto_id }}");

 timeInput.addEventListener('change', function() {
     const selectedTime = new Date(`2000-01-01T${timeInput.value}`);
     const now = new Date();
 
     if (selectedTime < now) {
         const hours = now.getHours().toString().padStart(2, '0');
         const minutes = now.getMinutes().toString().padStart(2, '0');
         timeInput.value = `${hours}:${minutes}`;
     }
 });

 setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);