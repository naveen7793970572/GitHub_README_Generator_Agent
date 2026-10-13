
import streamlit as st
from app import create_readme, get_insights

st.set_page_config(
    page_title="GitHub README Generator",
    page_icon="📘",
    layout="wide"
)

st.title("📘 GitHub README Generator Agent")
st.write(
    "Enter a public GitHub repository URL and let the AI "
    "analyze your project and generate a README.md."
)

st.divider()

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)


if st.button("📊 Analyze Repository", use_container_width=True):
    if not repo_url.strip():
        st.warning("Please enter a GitHub repository URL.")
    else:
        try:
            with st.spinner("Fetching repository insights..."):
                insights = get_insights(repo_url.strip())

            st.session_state["repo_insights"] = insights
            st.success("Repository analysis complete!")

        except Exception as error:
            st.error(f"Unable to analyze repository: {error}")

if st.session_state.get("repo_insights"):
    data = st.session_state["repo_insights"]

    st.subheader("📊 Repository Insights")
    st.write(f"**Repository:** [{data['name']}]({data['url']})")
    st.write(f"**Description:** {data['description']}")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⭐ Stars", data["stars"])
    col2.metric("🍴 Forks", data["forks"])
    col3.metric("📄 Files", data["total_files"])
    col4.metric("📁 Folders", data["total_folders"])

    st.write(f"**Default branch:** {data['default_branch']}")
    st.write(f"**Open issues:** {data['open_issues']}")
    st.write(f"**Created:** {data['created_at']}")
    st.write(f"**Last updated:** {data['updated_at']}")

    if data["languages"]:
        st.subheader("💻 Programming Languages")

        total_bytes = sum(data["languages"].values())

        if total_bytes:
            for language, byte_count in sorted(
                data["languages"].items(),
                key=lambda item: item[1],
                reverse=True,
            ):
                percentage = byte_count / total_bytes * 100
                st.write(f"**{language}:** {percentage:.1f}%")
                st.progress(percentage / 100)

    with st.expander("📂 Project Structure"):
        if data["folders"]:
            st.write("**Folders**")
            for folder in data["folders"]:
                st.text(f"📁 {folder}")

        st.write("**Files**")
        for path in data["files"]:
            st.text(f"📄 {path}")

        if data["truncated"]:
            st.warning(
                "GitHub returned a truncated file tree. "
                "The displayed structure may be incomplete."
            )

    with st.expander("📦 Dependency Files"):
        if data["dependency_files"]:
            for path in data["dependency_files"]:
                st.write(f"- `{path}`")
        else:
            st.info("No common dependency manifest was detected.")

            
generate = st.button(
    "🚀 Generate README",
    type="primary",
    use_container_width=True
)

if generate:
    if not repo_url.strip():
        st.warning("Please enter a GitHub repository URL.")

    else:
        try:
            with st.spinner(
                "Analyzing repository and generating README..."
            ):
                readme = create_readme(repo_url.strip())

            st.session_state["generated_readme"] = readme
            st.session_state["repo_url"] = repo_url.strip()

            st.success("README generated successfully!")

        except Exception as error:
            st.error(f"Unable to generate README: {error}")

if st.session_state.get("generated_readme"):
    readme = st.session_state["generated_readme"]

    st.divider()
    st.subheader("📄 Generated README")

    preview_tab, markdown_tab = st.tabs(
        ["Preview", "Markdown Source"]
    )

    with preview_tab:
        st.markdown(readme)

    with markdown_tab:
        st.code(readme, language="markdown")

    st.download_button(
        label="⬇️ Download README.md",
        data=readme,
        file_name="README.md",
        mime="text/markdown",
        use_container_width=True
    )

    st.caption(
        f"Source repository: {st.session_state.get('repo_url', '')}"
    )