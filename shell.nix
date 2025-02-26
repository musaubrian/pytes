{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3Packages.streamlit
    python3Packages.numpy
    python3Packages.opencv4
    python3Packages.pyperclip
    python3Packages.pytesseract
    tesseract
  ];
  shellHook = ''
    # exported variables maybe...
  '';
}
