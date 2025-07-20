<template>
  <div>
    <h2>Lista de empleados</h2>
    <table border="1">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Correo</th>
          <th>Rol</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.name }}</td>
          <td>{{ employee.email }}</td>
          <td>{{ employee.role }}</td>
          <td>
            <button @click="editEmployee(employee)">Editar</button>
            <button @click="deleteEmployee(employee.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const employees = ref([
  { id: 1, name: 'Juan Pérez', email: 'juan@empresa.com', role: 'Gerente' },
  { id: 2, name: 'María López', email: 'maria@empresa.com', role: 'Asistente' }
])

function editEmployee(employee) {
  alert(`Editar: ${employee.name}`)
}

function deleteEmployee(id) {
  const index = employees.value.findIndex(emp => emp.id === id)
  if (index !== -1) {
    employees.value.splice(index, 1)
  }
}
</script>
