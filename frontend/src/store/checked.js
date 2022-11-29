import { defineStore } from "pinia";

export const useCheckedStore = defineStore("checkedValues", {
  // total number of steps
  state: () => ({
    steps: Number,
    values: [
      {
        step: Number,
        type: String,
        choices: [],
      },
    ],
  }),

  getters: {
    getTotalSteps(state) {
      console.log("getTotalSteps", state.steps);
      return state.steps;
    },
    // get values
    getCurrentStepValues(state) {
      console.log("getCurrentStepValues", state.values);
      return state.values;
    },
    getChecked(state) {
      console.log("getChecked", state.values);
      return state.values;
    },
  },
  actions: {
    setTotalSteps(steps) {
      this.steps = steps;
    },
    setCurrentStep(step) {
      this.currentStep = step;
    },
    setChecked(values) {
      this.values = values;
    },
  },
});
