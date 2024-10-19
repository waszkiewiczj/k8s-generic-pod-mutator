{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      poetry
      kubectl
      kubernetes-helm
      k3d
    ];
}
