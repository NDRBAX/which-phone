import { reactive } from "vue";

export default function useForm() {
  const values = reactive({
    // Step 1
    firstname: "",
    lastname: "",

    // Step 2
    age: "",

    // Step 3
    description: "",
  });

  return {
    values,
  };
}
