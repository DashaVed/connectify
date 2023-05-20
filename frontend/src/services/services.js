import "dayjs/locale/ru";
import dayjs from "dayjs";


export default function formatDate(date) {
  dayjs.locale("ru");
  return dayjs(date).format("D MMMM YYYY г.");
}