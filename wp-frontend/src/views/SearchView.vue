<template>
  <div>
    <MultiStepForm v-bind:steps="steps" @devices="receiveDevices" />
    <CategoryFilters v-bind:data="resultDevices" />
  </div>
</template>

<script>
import MultiStepForm from "../components/MultiStepForm.vue";
import CategoryFilters from "../components/CategoryFilters.vue";
import { inject } from "vue";

export default {
  components: {
    MultiStepForm,
    CategoryFilters,
  },
  data() {
    return {
      steps: inject("dataENG").multiStepFormData,
      resultDevices: [],
      typeError: "",
      errors: [],
    };
  },
  methods: {
    receiveDevices(devices) {
      this.resultDevices = devices;
      if (devices.length === 0) {
        this.errors = [
          "No devices found. Please try again with different filters!",
        ];
        this.typeError = "error";
      } else {
        this.errors = [`Found ${devices.length} devices!`];
        this.typeError = "success";
      }
    },
    closeMessageError() {
      this.errors = [];
    },
  },
};
</script>
