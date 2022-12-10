import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";

export const useCheckedStore = defineStore({
  id: "checked",
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

    async submit() {
      let url = "/wphone/submit";
      let user = useAuthStore().getUser;
      let values = this.getAllValues;
      values.shift();
      let data = {};

      if (user === null) {
        data = {
          user: "guest",
          values: values,
        };
        console.log("values", values);
      } else {
        data = {
          user: user,
          values: values,
        };
      }

      let jsonData = JSON.stringify(data);
      let config = {
        withCredentials: false,
        headers: {
          "Content-Type": "application/json",
        },
      };
      await axios.post(url, jsonData, config);
    },
  },
});
