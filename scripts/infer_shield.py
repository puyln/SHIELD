from __future__ import annotations

from _common import build_parser, get_manifest, load_config, print_config, public_release_unavailable, validate_manifest


def main() -> None:
    parser = build_parser("Run SHIELD inference on an NC-MRI case manifest.")
    args = parser.parse_args()
    cfg = load_config(args.config)
    manifest = get_manifest(cfg, args.manifest)
    cases = validate_manifest(manifest)
    print(f"Validated {cases} manifest case(s) for inference.")
    if args.dry_run:
        print_config(cfg)
        return
    public_release_unavailable("Inference")


if __name__ == "__main__":
    main()
