<template>
  <div class="flex min-h-screen bg-gray-100">
    <aside class="w-64 bg-blue-900 text-white p-6 space-y-6">
      <h2 class="text-2xl font-bold mb-8">EmpleadosApp</h2>
      <nav class="flex flex-col space-y-3">
        <RouterLink
          to="/"
          class="block py-2 px-3 rounded hover:bg-blue-700"
          active-class="bg-blue-700"
          exact
        >
          Inicio 
        </RouterLink>
        <RouterLink
          to="/empleados"
          class="block py-2 px-3 rounded hover:bg-blue-700"
          active-class="bg-blue-700"
        >
          Empleados
        </RouterLink>
        <RouterLink
          to="/registro"
          class="block py-2 px-3 rounded hover:bg-blue-700"
          active-class="bg-blue-700"
        >
          Tarja
        </RouterLink>
      </nav>
    </aside>

    <main class="flex-1 p-6">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
