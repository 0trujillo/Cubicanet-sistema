<!-- src/components/EmpleadoForm.vue -->
<template>
  <div>
    <h2 class="text-lg font-bold mb-2">Formulario de Empleado</h2>
    <!-- Aquí va el formulario -->
  </div>
</template>

<script>
export default {
  props: ['empleadoEditado'],
  emits: ['recargar'],
  data() {
    return {
      // campos para el formulario
    };
  }
};
</script>
