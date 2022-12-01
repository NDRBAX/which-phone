import { defineStore } from "pinia";

export const useCheckedStore = defineStore({
  id: "checked",
  // state to be used by the store for the checked items by step and by question
  state: () => ({
    values: [
      {
        step: null,
        question: [
          {
            label: null,
            checked: [],
          },
        ],
      },
    ],
  }),

  getters: {
    getCheckedByStep: (state) => (step) => {
      return state.values[step].question;
    },
    getAllValues: (state) => {
      // console.log("state.values", state.values);
      return state.values;
    },
  },
  actions: {
    setCheckedByStep(step, label, checked) {
      // check if step exists
      if (this.values[step]) {
        // remove the step
        this.values.splice(step, 1);
        this.values.splice(step, 0, {
          step: step,
          question: [
            {
              label: label,
              checked: checked,
            },
          ],
        });
      } else {
        this.values[step] = {
          step: step,
          question: [
            {
              label: label,
              checked: checked,
            },
          ],
        };
      }
      console.log(this.getAllValues);
    },
  },
});
