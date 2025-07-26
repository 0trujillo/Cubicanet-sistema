<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Gestión de Empleados</h1>

    <!-- Botón agregar -->
    <div class="mb-4">
      <button
        class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-xl shadow"
      >
        + Agregar Empleado
      </button>
    </div>

    <!-- Tabla empleados -->
    <div class="overflow-x-auto bg-white rounded-2xl shadow">
      <table class="min-w-full text-left border-collapse">
        <thead class="bg-gray-200 text-gray-700">
          <tr>
            <th class="px-6 py-4 font-semibold">Nombre</th>
            <th class="px-6 py-4 font-semibold">Cargo</th>
            <th class="px-6 py-4 font-semibold">Fecha de Ingreso</th>
            <th class="px-6 py-4 font-semibold text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr class="hover:bg-gray-50 border-b">
            <td class="px-6 py-4">María López</td>
            <td class="px-6 py-4">Administrativa</td>
            <td class="px-6 py-4">2023-08-15</td>
            <td class="px-6 py-4 text-center space-x-2">
              <button class="text-yellow-500 hover:text-yellow-600 font-medium">Editar</button>
              <button class="text-red-500 hover:text-red-600 font-medium">Eliminar</button>
            </td>
          </tr>
          <!-- Puedes duplicar más filas estáticas -->
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
// Sin lógica aún
</script>

<style scoped>
/* No necesitas CSS personalizado gracias a Tailwind */
</style>
