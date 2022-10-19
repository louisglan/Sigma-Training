import { assertEquals } from "https://deno.land/std/testing/asserts.ts";
import { capitalise } from "./tdd_prework.js";

Deno.test("full name with one name is capitalised", () => {
  assertEquals(capitalise("John"), "JOHN");
});

Deno.test("full name with four names correctly capitalised", () => {
  assertEquals(
    capitalise("Maya Alice Jane Johnson"),
    "MAYA ALICE JANE JOHNSON"
  );
});

Deno.test("no name returns nothing", () => {
  assertEquals(capitalise(""), "");
});

// A full name with one name is being correctly capitalised, e.g. a first name.
// A full name with four names is being correctly capitalised, e.g. "Maya Alice Jane Johnson"
// No name returns nothing, e.g. "".
