import { defineStore } from "pinia";

export const useCsrfTokenStore = defineStore({
  id: "csrftoken",
  state: () => ({
    csrfToken: null,
  }),

  getters: {
    getCsrfToken: (state) => {
      return state.csrfToken;
    },
  },

  actions: {
    setCsrfToken(csrfToken) {
      this.csrfToken = csrfToken;
      localStorage.setItem("csrfToken", csrfToken);
    },
  },
});
