import { defineStore } from "pinia";

export const useFormStore = defineStore("formStore", {
  state: () => ({
    firstname: "Andre",
    lastname: "",
    age: 29,
    description: "",
  }),
});
