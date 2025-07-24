<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Panel de Empleados</h1>

    <!-- Tarjetas resumen -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
      <div class="bg-white shadow-lg rounded-2xl p-6 border-l-8 border-blue-500">
        <h2 class="text-xl font-semibold text-gray-700">Empleados activos</h2>
        <p class="text-4xl font-bold text-blue-600 mt-2">32</p>
      </div>

      <div class="bg-white shadow-lg rounded-2xl p-6 border-l-8 border-green-500">
        <h2 class="text-xl font-semibold text-gray-700">En turno</h2>
        <p class="text-4xl font-bold text-green-600 mt-2">12</p>
      </div>

      <div class="bg-white shadow-lg rounded-2xl p-6 border-l-8 border-red-500">
        <h2 class="text-xl font-semibold text-gray-700">Fuera de turno</h2>
        <p class="text-4xl font-bold text-red-600 mt-2">20</p>
      </div>
    </div>

    <!-- Placeholder para futuras gráficas o tabla -->
    <div class="bg-white rounded-2xl shadow p-6 text-center text-gray-500">
      <p>Próximamente: gráfica de asistencia o tabla de resumen</p>
    </div>
  </div>
</template>

<script setup>
// Sin lógica por ahora
</script>

<style scoped>
/* No necesario por usar Tailwind */
</style>
