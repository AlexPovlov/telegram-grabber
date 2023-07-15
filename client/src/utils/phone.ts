import { Mask } from "maska";

export function displayPhone(phone: string) {
  return new Mask({ mask: "+# (###) ### ## ##" }).masked(phone);
}
