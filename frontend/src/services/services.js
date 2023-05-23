import "dayjs/locale/ru";
import dayjs from "dayjs";


export default function formatDate(date, format="D MMMM YYYY г.") {
  dayjs.locale("ru");
  return dayjs(date).format(format);
}