<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-4">Gestión de Empleados</h1>
    <EmpleadoForm :empleadoEditado="empleadoSeleccionado" @recargar="cargarEmpleados" />
    <EmpleadoTabla :empleados="empleados" @editar="seleccionarEmpleado" @eliminar="eliminarEmpleado" />
  </div>
</template>

<script>
import axios from 'axios';
import EmpleadoForm from '@/components/EmpleadoForm.vue';
import EmpleadoTabla from '@/components/EmpleadoTabla.vue';

export default {
  components: { EmpleadoForm, EmpleadoTabla },
  data() {
    return {
      empleados: [],
      empleadoSeleccionado: null
    };
  },
  methods: {
    async cargarEmpleados() {
      const res = await axios.get('http://localhost:5000/api/empleados');
      this.empleados = res.data;
    },
    seleccionarEmpleado(emp) {
      this.empleadoSeleccionado = { ...emp };
    },
    async eliminarEmpleado(id) {
      await axios.delete(`http://localhost:5000/api/empleados/${id}`);
      this.cargarEmpleados();
    }
  },
  mounted() {
    this.cargarEmpleados();
  }
};
</script>
