import { defineStore } from "pinia";

export const useFormValues = defineStore("formValues", {
  state: () => ({
    firstname: "",
    lastname: "",
    age: 0,
    description: "",
  }),
});
