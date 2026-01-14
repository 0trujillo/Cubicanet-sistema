<!-- src/components/EmpleadoTabla.vue -->
<template>
  <table class="min-w-full bg-white rounded shadow">
    <thead>
      <tr class="bg-gray-100 text-gray-700">
        <th class="p-3 text-left">ID</th>
        <th class="p-3 text-left">Nombre</th>
        <th class="p-3 text-left">Cargo</th>
        <th class="p-3 text-left">Salario</th>
        <th class="p-3 text-left">Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="emp in empleados"
        :key="emp.id"
        class="border-t hover:bg-gray-50"
      >
        <td class="p-3">{{ emp.id }}</td>
        <td class="p-3">{{ emp.nombre }}</td>
        <td class="p-3">{{ emp.cargo }}</td>
        <td class="p-3">{{ emp.salario }}</td>
        <td class="p-3 space-x-2">
          <button @click="$emit('editar', emp)" class="text-blue-600 hover:underline">Editar</button>
          <button @click="$emit('eliminar', emp.id)" class="text-red-600 hover:underline">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ['empleados']
};
</script>
